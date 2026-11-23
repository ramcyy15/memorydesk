from ask import answer_question, supabase


if __name__ == "__main__":
    email = "ana@brightbakery.test"
    found = supabase.table("customers").select("*").eq("email", email).execute()

    if not found.data:
        created = supabase.table("customers").insert({
            "email": email,
            "name": "Ana",
        }).execute()
        customer_id = created.data[0]["id"]
        print("New customer created.")
    else:
        customer_id = found.data[0]["id"]
        print("Existing customer found.")

    print("Customer id:", customer_id)

   
    conversation = supabase.table("conversations").insert({
        "customer_id": customer_id,
    }).execute()
    conversation_id = conversation.data[0]["id"]
    print("Conversation id:", conversation_id)

    while True:
        customer_message = input("Message: ").strip()

        if customer_message.lower() == "end":
            break               
        if not customer_message:
            continue            

        
        saved = supabase.table("messages").insert({
            "conversation_id": conversation_id,
            "role": "customer",
            "content": customer_message,
        }).execute()
        message_id = saved.data[0]["id"]  

        agent_message = answer_question(customer_message)
        print(agent_message)

        supabase.table("messages").insert({
            "conversation_id": conversation_id,
            "role": "agent",
            "content": agent_message,
        }).execute()
