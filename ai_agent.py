import os
import google.generativeai as genai
import time

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_task_plan(task_description):
    try:
        print("\nGenerating a step-by-step plan... Please wait.")
        time.sleep(2)  
        model = genai.GenerativeModel('gemini-2.0-flash')
        response = model.generate_content(f"Provide a step-by-step plan to: {task_description}")
        return response.text
    except Exception as e:
        print(f"Error generating task plan: {e}")
        return "Error: Unable to generate task plan."

def main():
    task = input("Describe the task you want to automate: ")
    while True:
        print("\nProcessing your input... Please wait.")
        time.sleep(2) 
        plan = get_task_plan(task)
        print("\nProposed Plan:\n")
        print(plan)
        approval = input("\nDo you approve this plan? (yes/no): ").strip().lower()
        if approval == 'yes':
            print("\nPlan approved. Exiting.")
            break
        elif approval == 'no':
            reason = input("Please provide the reason for disapproval: ")
            print("\nRefining the plan based on your feedback... Please wait.")
            time.sleep(2) 
            task = f"{task}. Note: {reason}" 
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()