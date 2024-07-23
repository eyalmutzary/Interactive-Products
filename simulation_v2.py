from setting_generator import run_prompt
from time import sleep

setting = f"""
    **Setting:**

    The secluded, luxurious Villa Serenity, situated on a large plot of land in the French Riviera, offers breathtaking views of the Mediterranean Sea and a private beach. The villa's interior features a spacious living room, a fully equipped kitchen, multiple bedrooms, and bathrooms. The unique features include:

    * A state-of-the-art entertainment system with a large screen and top-notch audio equipment
    * A gym and fitness area
    * A private movie theater
    * A beautifully landscaped garden and swimming pool
    * A private beach access with a beachside bar and grill

    However, the villa has some limitations and challenges:

    * No cell phone signal or internet connection within the villa, limiting external communication
    * A high-security perimeter fence and 24/7 camera surveillance reinforce the villa's isolation
    * The electricity supply is limited, relying on generator backup during peak usage hours
    * The main water source is a well, which can be affected by seasonal changes and occasional droughts

    To enhance realism and interaction opportunities:

    * The villa's private beach and surrounding greenery can be used for outdoor activities, such as yoga, meditation, or even a game of beach volleyball
    * The garden and swimming pool can host gatherings and casual events, fostering social interaction and relaxation

    **Character Adjustments:**

    * Alex Chen: Added a new background detail - a sports injury that requires rehabilitation during the simulation, potentially affecting his competitive nature
    * Rachel Patel: Changed her background from a nurse to a medical researcher, allowing her to contribute to medical discussions and debates
    * Naomi Lee: Emphasized her competitive nature by introducting a rivalry with Sophia Rodriguez, a skilled chef, in the kitchen
    * Ariana Rodriguez: Introduced a personal struggle, such as a past trauma or ongoing health issue, to add depth to her character and relationships with others
    * Jack Harris: Changed his background from a musician to a music producer, allowing him to bring a unique perspective to the group and potentially create new conflicts or opportunities
    * Sophia Martinez: Introduced her artistic skills by adding a photography hobby, which can be used to create a creative outlet and share with the group
    * Sophia Rodriguez: Added a personal secret - a hidden passion for writing - which can be revealed and explored throughout the simulation

    These changes enrich the characters, relationships, and dynamics, setting the stage for a more realistic and engaging simulation.

"""

def generate_next_hour(setting, event_history, time_of_day):
    # past_hours = ''.join([hour+'\n' for hour in event_history[-5:]])
    past_hours = ''.join(event_history[-5:])
    prompt = f"""
        You are to continue a real-life simulation involving a group of characters with diverse personalities and relationships who are confined to the same location for an extended period. The goal is to generate realistic and logical events over time, focusing on ordinary interactions rather than dramatic storytelling.

        **Parameters for Describing Events:**
        1. **Consistency with Characters:**
           - Events should be consistent with the characters' personalities, backgrounds, and relationships.
           - Characters' actions and reactions should be believable and grounded in their established traits.

        2. **Logical Event Progression:**
           - Events should unfold naturally based on the previous hours and the current situation.
           - Prioritize everyday occurrences and interactions that reflect real-life dynamics.

        3. **Realistic Interactions:**
           - Focus on realistic interactions and conversations among the characters.
           - Avoid overly dramatic or implausible scenarios unless they arise naturally from the situation.

        **Current Setting and Recent Events:**
        **Current Time of Day:** {time_of_day}

        - **Setting:**:
        {setting}

        - **Events of the Last Hours:**
        {past_hours}

        {f'** Important tip I give you to make it more interesting and you should follow: {tips_to_make_it_interesting[-1]}'}


        ** Additional Instructions: **
        Based on the current setting and the past events, describe what happens in the next hour.
        Ensure the description adheres to the principles of consistency, logical progression, and realism.
        Highlight any significant interactions or developments among the characters, and consider their personalities and relationships when detailing their actions and reactions.
        Please make it concise and not too long.
        Pay attention to the time of the day.
        dont mention the time of the day in the event description.
    """
    return run_prompt(prompt)





def judge_interestingness():
    prompt1 = f"""
        You are tasked with evaluating the interest level of a real-life simulation involving a group of characters with diverse personalities and relationships who are confined to the same location for an extended period. The goal is to assess whether the simulation is interesting from your perspective.

        **Parameters for Evaluating Interest:**
        1. **Character Dynamics:**
           - The complexity and depth of interactions between characters.
           - Development of relationships, including conflicts, alliances, and evolving dynamics.

        2. **Event Variety:**
           - The range and diversity of events and activities.
           - Balance between ordinary occurrences and notable developments.

        3. **Engagement and Realism:**
           - How engaging and believable the events and interactions are.
           - Consistency with real-life scenarios and logical progression of events.
           - Is the time of day fits the events? e.g - are they sleeping at night, etc.

        **Current Setting and Recent Events:**
        - **Setting:**
        {setting}
        - **Events of the Last 10 Hours:**
        {''.join(event_history[-10:])}

        **Instructions:**
        Based on the current setting and the events of the past hours, evaluate whether the simulation so far is interesting.
        Provide a rating from 1 to 100, where 1 is not interesting at all and 100 is extremely interesting.
        Explain your rating by detailing why the simulation is or is not interesting, considering the character dynamics, variety of events, and overall engagement and realism.
        Please be critical. If you think it's boring, say so. If you think it's engaging, explain why.

    """

    # prompt2 = f"""
    #     You are given a certian events in a simulation. you should decide if the event is interesting or not with a number from 0-100.
    #     please explain your choice.
    #
    #     **Current Setting and Recent Events:**
    #     - **Setting:**
    #     {setting}
    #     - **Events of the Last 10 Hours:**
    #     {''.join(event_history[-10:])}
    #
    #
    # """
    return run_prompt(prompt1)


def second_LLM(last_result):
    # here it should get the last result of the last hour, and modify it so it will be much more logical.
    prompt = f"""
            You are to continue a real-life simulation involving a group of characters with diverse personalities and relationships who are confined to the same location for an extended period. The goal is to generate realistic and logical events over time, focusing on ordinary interactions rather than dramatic storytelling.
            your task is to modify the last event to make it more logical and realistic.
            E.g: if it is the middle of the night, probably the characters are sleeping, not having a party.
            E.g: if a character is a vegetarian, he probably won't eat a steak.
            E.g: if the tension between two characters is high, there might be a conflict between them at some point.
            
            You should return the modified event in a similar format to the last event.
            Please dont add an introduction or any other text, just the modified event.
            
            **Last event**:
            {last_result}
            """
    return run_prompt(prompt)




event_history = []
tips_to_make_it_interesting = ['']

def run_simulation(setting, hours=24):
    start_time = 0
    is_pm = True
    for hour in range(1, hours + 1):
        current_time = str((start_time + hour) % 12) + ('pm' if is_pm else 'am')
        event = second_LLM(generate_next_hour(setting, event_history, current_time))
        event_history.append(f"Previously, at {current_time}: {event} \n \n")

        print(f"Previously, at {current_time}: {event}")
        print("\n" + "-" * 50 + "\n")

        if hour % 4 == 0:
            tips_to_make_it_interesting.append(judge_interestingness())
            print(tips_to_make_it_interesting[-1])
            print("\n" + "-" * 50 + "\n")

        if hour % 12 == 0:
            is_pm = not is_pm
        sleep(5)  # Wait 5 seconds between events


run_simulation(setting, 24)  # Run for 24 hours