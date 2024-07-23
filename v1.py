# from huggingface_hub import InferenceClient
#
# API_TOKEN = "*********************************"
#
# client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct",token=API_TOKEN)
#
# for message in client.chat_completion(
# 	messages=[{"role": "user", "content": "Explain quantum physics to me in simple terms."}],
# 	max_tokens=2000,
# 	stream=True,
# ):
#     print(message.choices[0].delta.content, end="")
#



from huggingface_hub import InferenceClient
import time

API_TOKEN = "*********************************"
client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct",token=API_TOKEN)

event_history = []

def generate_highly_detailed_setting():
    prompt = f"""
            Hi there! I'm working on a simulation project where a group of characters interact within a specific environment. I'd love your help in crafting an engaging setting and defining unique characters that will lead to interesting stories.
            
            **Setting:**
            
            * **Genre:** It should be a realistic setting of the current world.
            * **Tension Factor:** Aim to introduce a single and specific central tension that drives the characters' actions and creates conflict. This could be:
                * **Resource Scarcity:** Limited access to a vital resource like water, food, or energy. It could be a less significant resource like bedding (for example, in a house scene).
                * **Social Hierarchy:** A rigid social structure with limited mobility and potential for rebellion.
                * **External Threat:** A looming danger like an approaching storm, a hostile environment, or a rival group.
                * **Mystery/Puzzle:** An unsolved problem or hidden secret that motivates characters to collaborate.
            * **Details:** Describe the setting in more detail, considering elements like:
                * **Geography:** where are they? how does the outside world look like?
                * **Technology Level:** technology of the current world.
                * **Social Structure:** Are there established factions, classes, or power dynamics?
                * **Visuals:** Paint a picture of the environment with details about architecture, natural features, or unique elements. 
                * Note: The setting itself should be a small place, like a room, a house, where the characters are stuck for some reason and have to interact with each other
                
            **Characters:**
            
            * **Number:** Let's create a group of 3-4 characters.
            * **Personalities:** For each character, define a distinct personality with traits like:
                * **Leader/Follower:** Does the character take charge or prefer to follow others?
                * **Optimist/Pessimist:** Does the character see the glass as half full or half empty?
                * **Cautious/Reckless:** Does the character take calculated risks or act impulsively?
                * **Selfless/Self-Serving:** Does the character prioritize the group's well-being or their own goals?
                Please feel free to add more traits or personality dimensions as needed.
            * **Skills:** Give each character a unique skillset that contributes to the group's dynamic:
                * **Strength/Agility:** Physical capabilities for fighting or tasks requiring physical prowess.
                * **Intelligence/Knowledge:** Expertise in a specific field like engineering, medicine, or leadership.
                * **Charisma/Deception:** Ability to influence others through persuasion or manipulation.
                * **Empathy/Ruthlessness:** Capacity for compassion and understanding or a cold, calculating nature.
                Please feel free to add more skills as needed. 
            * **Relationships:** Briefly describe any initial relationships between characters (friends, rivals, strangers, etc.).
            Notice:  Please make the characters be kinda of real people, with flaws and virtues, and not just stereotypes and cliches.
            
            ** TIPS:
             * The overall situation should be LOGICAL and REALISTIC. for example, if they are in a tv show, there shouldn't be shortage of food or water, but instead other challenges 
             * please describe how these characters got into this situation and why they are stuck in this place. 
             * The situation the charcters are in should be not very rare. The reader should be able to relate to it, and feel like it could happen to them.
             * The characters might be in a situation they put themselves in. for example, a reality show or a social experiment.
             * dont be a cliché, dont create a generic setting, dont create stereotypes
             * Dont create a too hard setting, or too easy, try to make it balanced. the simulation should be with increasing difficulty overtime. it shouldn't start too hard.
             * the goal is to create a setting that feels immersive and generates tension for the characters. The characters themselves should be diverse in personality and skills, with the potential for cooperation, conflict, and unexpected alliances.
             * your answer will be copied as-is so make sure to format it properly and dont include any instructions in the answer.
            """
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500,
        stream=False
    )
    return response.choices[0].message.content

def generate_less_detailed_setting():
    prompt = f"""
    Genre: Realistic, current world.
    Tension Factor: Describe a single, central challenge that forces characters to interact and creates conflict. This could be ONLY ONE SPECIFIC of the following:
    Limited resources: Food, water, communication, or something more unexpected. (in case chose this, please choose one and specify the resource)
    External threat: A looming danger, like a natural disaster, hostile environment, or unseen force.
    Mystery/Puzzle: An unsolved problem or hidden secret that motivates characters to collaborate.
    Normal: missing a bed, a broken window, a locked door, a missing item, etc.
    Characters:
    Number: 3-4 diverse individuals with distinct personalities and skills.
    Focus: Highlight key personality traits and skills that could lead to conflict and cooperation.
    Relationships: Briefly describe their initial connections (do they knew each other before? if so, how is their relationship? couple, lovers, strangers, acquaintances, rivals?).
    Setting:
    Location: Describe a small, confined space where the characters are stuck (e.g., elevator, train car, abandoned building, reality TV show, social experience etc).
    Overall Tone: Aim for a realistic and immersive environment that fosters tension.
    Remember:
    Dont be cliché: Avoid stereotypes and generic settings. Create unique and engaging characters and situations.
    Not extreme or rare: The situation should be relatable and not too far-fetched. for the naked eye, it should seem like a normal situation on the surface.
    Logical and relatable: The situation should feel believable and something players can connect with. Also, the tension factor should be something that could happen in that situation.
    Increasing difficulty: Start with a manageable challenge and gradually introduce complications.
    Character potential: Diverse personalities and skills should create opportunities for conflict, cooperation, and unexpected alliances.
"""
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500,
        stream=False
    )
    return response.choices[0].message.content

possible_setting1 = """
    **Setting:**
    
    The setting is a small, confined, and underground nuclear bunker located beneath an abandoned factory in the heart of a dense, urban city. The bunker, known as "The Haven," was built in the 1980s as a safe haven for city officials and emergency responders in the event of a nuclear attack. The bunker is designed to sustain up to 50 people for up to two weeks.
    
    The tension factor in this setting is a mystery. A week ago, a group of strangers was randomly selected and brought to The Haven, with no knowledge of each other or their purpose. The group is confined to the bunker, with no communication with the outside world, and must work together to survive. The bunker's systems are malfunctioning, and the group soon discovers that the air filtration system is shutting down, making it imperative to find a solution quickly.
    
    The geography of The Haven is cramped and claustrophobic, with narrow corridors and small rooms. The technology level is current, with modern medical equipment and communication devices, but the systems are malfunctioning due to power outages and equipment failure.
    
    The social structure in The Haven is a mix of individuals with different backgrounds and skills. There are no established factions, but the group is forced to work together to survive. The architectural design of the bunker provides little natural light, creating an atmosphere of claustrophobia and isolation.
    
    Initial time of the day: 6:00 PM
    
    **Characters:**
    
    There are four characters in The Haven:
    
    1. **Alex Chen**: A 30-year-old engineer with expertise in electrical systems and mechanical repair. Alex is cautious, analytical, and selfless. She prioritizes the group's well-being and is driven to find a solution to the bunker's malfunctioning systems.
    
    Alex is a natural leader and takes charge of the group's efforts to repair the bunker. She is initially optimistic but becomes increasingly frustrated as time passes and the challenges mount.
    
    2. **Jesse "JD" Daniels**: A 25-year-old former soldier with combat training and tactical expertise. JD is a natural-born leader, but he is also reckless and impulsive. He is initially confrontational and resistant to authority, but as the situation becomes more dire, he begins to work with the group.
    
    JD is charismatic and has a strong sense of loyalty, which can sometimes borderline on ruthlessness. He is fiercely protective of the group and is driven to keep them safe.
    
    3. **Dr. Sophia Patel**: A 40-year-old psychologist with expertise in trauma counseling and human behavior. Sophia is empathetic, compassionate, and perceptive. She is initially hesitant to take charge, but as the group faces challenges, she becomes more assertive and helps to facilitate communication and cooperation.
    
    Sophia is a natural peacemaker and is driven to help the group work together and heal from their individual traumas.
    
    4. **Maya Ramos**: A 28-year-old artist with no technical expertise, but a strong sense of intuition and creativity. Maya is optimistic, open-minded, and intuitive. She is initially hesitant to participate in the group's efforts, but as the situation becomes more desperate, she begins to contribute with her unique perspective and skills.
    
    Maya is a gentle soul, but she is also fiercely independent and can come across as aloof or standoffish. She is driven to find a way out of The Haven and to explore the mystery behind their confinement.
    
    **Relationships:**
    
    Initially, the group is hesitant to work together, with Alex and JD immediately clashing due to their different personalities. Sophia attempts to mediate the conflict, while Maya observes from the sidelines, not wanting to draw attention to herself.
    
    As time passes, the group begins to form alliances and work together, but tensions and conflicts arise, forcing them to confront their differences and challenges. The characters' relationships are complex and multifaceted, with moments of cooperation, conflict, and unexpected alliances.
    
    The characters are stuck in The Haven due to a social experiment or reality show gone wrong. The situation is not unique, but it is relatable, as people are often confined to small spaces for extended periods due to natural disasters, medical emergencies, or military operations. The setting provides ample opportunities for tension and conflict, as the group struggles to survive and uncover the truth behind their confinement.

"""
possible_setting2 = """
    **Tension Factor:** Limited Resources (Food)
    
    **Characters:**
    
    1. Maya, a 28-year-old freelance writer, resourceful and determined, but struggling with chronic anxiety.
    2. Jake, a 32-year-old software engineer, logical and practical, but has a track record of being emotionally distant.
    3. Leila, a 25-year-old artist, creative and empathetic, but has a history of reckless decisions.
    4. Alex, a 35-year-old journalist, assertive and analytical, but has a tendency to dominate conversations.
    
    **Relationships:** The characters all attend the same social networking event, where they meet and strike up conversations. They're acquaintances, but not close friends. Maya and Leila have a history of collaborating on projects, while Jake and Alex have a mutual friend. Alex and Maya had a brief romantic fling a few years ago, but it ended amicably.
    
    **Setting:** A small, luxurious conference room within a high-tech skyscraper. The doors are locked due to a power outage in the building, and the characters are trapped for the night.
    
    **Overall Tone:** A sense of unease settles in as the characters realize they're stuck, and their initial friendly conversation turns tense as they confront the reality of their situation.
    
    **Challenge:** The power outage has left the conference room without light, water, or working communication devices. The characters have only a few snacks and a dwindling supply of water. As the night wears on, they must work together to find a way to escape, ration their resources, and deal with the stress and anxiety of being trapped.
    
    **Conflict Potential:**
    
    * Maya's anxiety spikes as the situation becomes more dire, causing her to become more withdrawn and paranoid.
    * Jake's practical approach clashes with Leila's artistic thinking, leading to disagreements on how to tackle the problem.
    * Alex's assertive personality may come across as dominating, causing tension with the others, especially Maya, who feels he's disregarding her ideas.
    * Leila's tendency to take risks could cause the group to split on how to proceed, with some members favoring a more cautious approach.
    
    **Unfolding Complications:**
    
    * As the night wears on, the characters may start to experience physical symptoms of dehydration, fatigue, and hunger, making it more challenging to work together.
    * The lack of communication devices could lead to misunderstandings and miscommunications, further exacerbating tensions within the group.
    * As midnight approaches, the characters may become more desperate, leading to flashpoints of panic, anger, and hysteria.
    
    This scenario offers a relatable and realistic setup, with characters that are distinct and complex, creating opportunities for both conflict and cooperation. The limited resources and confined setting increase tension, making it a compelling and immersive experience.
"""
# print(generate_less_detailed_setting())

def generate_event(hour, event_history):
    context = "\n".join(event_history[-5:])  # Use last 5 events for context
    prompt = f"""Hour {hour} since the beginning of the story. 
    
    Initial situation:
    {possible_setting2}
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


# setting = generate_highly_detailed_setting()
# print(setting)


def run_simulation(hours):
    for hour in range(1, hours + 1):
        event = generate_event(hour, event_history)
        event_history.append(f"Hour {hour}: {event}")

        print(f"Hour {hour}:")
        print(event)
        print("\n" + "-" * 50 + "\n")
        time.sleep(5)  # Wait 5 seconds between events

run_simulation(24)  # Run for 24 hours