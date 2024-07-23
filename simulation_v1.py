from huggingface_hub import InferenceClient
import time

API_TOKEN = "*************************"
client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", token=API_TOKEN)

event_history = []


def generate_event_v3(hour, setting, event_history):
    context = "\n".join(event_history[-5:])  # Use last 5 events for context
    prompt = f"""Hour {hour} since the beginning of the story.

    Initial situation:
    {setting}
    Previous events:
    {context}

    Based on these previous events, describe what had happened in the past hour. There might be very insignificant and boring events, but the could be some plot twists, aliances or conflicts. In rare times, with the correct setting, some extreme behaviors could happen (like murder etc). Also something in the environment could unexpectedly happen and change the whole situation.
    I want the plot to be developing and the characters to be evolving. But also, the events should be realistic and not too far-fetched.
    In times where the pressure and tention is boiling, there must be a dramatic event that would change everything.
    And also, the simulation is long, so the events should be escalating in difficulty and tension slowly over time, and not too drastically or dramatic.
    You don't have to mention every character and every detail.
    You dont have to refer to every character's skills and traits, but you can if you want to.
    only mention the most important events and interactions.
    Focus on their interactions, how their traits influence their actions, and how this event follows from or relates to previous events.
    Dont get too long in your description. Keep it concise and to the point. if some big events happened, than describe them with more details.
    The first line should be the most important event that happened in the past hour.
    no introduction or conclusion is needed.
    """

    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        stream=False
    )

    return response.choices[0].message.content


def generate_event_v1(hour, setting, event_history):
    context = "\n".join(event_history[-5:])  # Use last 5 events for context
    prompt = f"""Hour {hour} since the beginning of the story.

    Initial situation:
    {setting}
    Previous events:
    {context}


    Based on these previous events, describe what had happened in the past hour. Focus on their communication and events. No introduction needed.
    In case the plot becomes boring, you could include unexpected behaviors of the characters (but keep it logical to the situation).
    Keep it short and concise.
    """

    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        stream=False
    )

    return response.choices[0].message.content

setting = """
    **Setting:** A small, rustic cabin on a remote mountain trail. The cabin is surrounded by dense forest, with steep cliffs on one side and a raging river on the other. The only way in or out is a narrow, winding path that's prone to landslides and rockfall.

    **Characters:**
    1. **Dr. Sophia Patel**: A 35-year-old geologist from India, Sophia is the group's leader. She's a no-nonsense, confident woman with a wealth of knowledge about the local geology. Sophia is determined and resourceful, but her strong sense of responsibility can sometimes make her come across as aloof or controlling.
    2. **Jesse "Hawk" Hawkins**: A 28-year-old park ranger from the US, Hawk is a rugged outdoorsman with a love for adventure and the great beyond. He's charming, witty, and has a natural charisma that puts people at ease. Hawk is also fiercely protective of his team and will stop at nothing to keep them safe.
    3. **Ramesh "Ram" Kumar**: A 32-year-old software engineer from India, Ram is a quiet, introspective man who's more at home with code than the wilderness. He's a bit of a introvert and can be hesitant to speak up, but once you get to know him, he's fiercely loyal and has a dry sense of humor.
    4. **Maya Singh**: A 25-year-old environmental activist from Canada, Maya is passionate about preserving the natural world. She's fiercely idealistic and can come across as a bit dogmatic, but she's also deeply compassionate and will fight tooth and nail for what she believes in.
    5. **Captain James "Jim" Reed**: A 45-year-old retired army captain from the US, Jim is a burly, imposing man with a no-nonsense attitude. He's a natural leader, but his bluntness and tendency to micromanage can sometimes put people on edge.

    **Relationships:**
    * Sophia and Hawk have a long history, having worked together on various expeditions before, and have developed a deep trust and respect for each other.
    * Ram is a recent addition to the group, having been recruited by Sophia to help analyze some geological data. He's still getting to know the others, but he looks up to Hawk as a mentor.
    * Maya and Jim have a tense relationship, as they disagree strongly on the role of humans in the natural world. Maya sees Jim as dismissive and short-sighted, while Jim views Maya as idealistic and impractical.
    * Sophia and Ram share a dry, witty sense of humor and often partner up on tasks.

    **Tension Factor:** The group's difficult situation is compounded by conflicting personalities and differing values. Sophia and Jim are constantly butting heads over how to navigate the situation, while Ram struggles to keep up with Hawk's adventurous spirit. Maya is increasingly frustrated with the group's lack of progress and apathy towards the environmental devastation caused by the natural disaster.

    As the days turn into weeks, tensions come to a head. The group's food supply is running low, and they're beginning to run out of clean water. Rivalries and interests are starting to boil over, and the already-frayed relationships between the characters are beginning to fray even further. As the weather worsens and the prospects of escape seem increasingly remote, will the group be able to work together to survive, or will their differences tear them apart?
"""

def run_simulation(setting, hours=24):
    for hour in range(1, hours + 1):
        event = generate_event_v1(hour, setting, event_history)
        event_history.append(f"Hour {hour}: {event}")

        print(f"Hour {hour}:")
        print(event)
        print("\n" + "-" * 50 + "\n")
        time.sleep(5)  # Wait 5 seconds between events


run_simulation(setting, 24)  # Run for 24 hours


