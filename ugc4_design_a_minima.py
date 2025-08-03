Python
"""
Design a Minimalist Chatbot Tracker

This project aims to create a simple chatbot tracker that records and displays conversation history.
The tracker will maintain a list of conversations, each represented by a unique ID.
Each conversation will have a chat history, which is a list of chat messages.

"""

class ChatbotTracker:
    """
    This class represents the chatbot tracker.
    It has a dictionary to store conversations, where each key is a unique conversation ID.
    Each conversation is represented by a dictionary with a chat history (list of messages).
    """

    def __init__(self):
        self.conversations = {}

    def add_conversation(self, convo_id):
        """
        Add a new conversation to the tracker.
        :param convo_id: Unique conversation ID
        :return: None
        """
        self.conversations[convo_id] = {"chat_history": []}

    def add_message(self, convo_id, message):
        """
        Add a new message to a conversation.
        :param convo_id: Unique conversation ID
        :param message: Message to be added
        :return: None
        """
        if convo_id in self.conversations:
            self.conversations[convo_id]["chat_history"].append(message)
        else:
            print("Conversation not found.")

    def view_conversation(self, convo_id):
        """
        Display the chat history of a conversation.
        :param convo_id: Unique conversation ID
        :return: None
        """
        if convo_id in self.conversations:
            for message in self.conversations[convo_id]["chat_history"]:
                print(message)
        else:
            print("Conversation not found.")

tracker = ChatbotTracker()

while True:
    print("\nChatbot Tracker Menu:")
    print("1. Add Conversation")
    print("2. Add Message")
    print("3. View Conversation")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        convo_id = input("Enter conversation ID: ")
        tracker.add_conversation(convo_id)
    elif choice == "2":
        convo_id = input("Enter conversation ID: ")
        message = input("Enter message: ")
        tracker.add_message(convo_id, message)
    elif choice == "3":
        convo_id = input("Enter conversation ID: ")
        tracker.view_conversation(convo_id)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")