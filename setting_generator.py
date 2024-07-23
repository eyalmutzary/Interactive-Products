from huggingface_hub import InferenceClient

API_TOKEN = "************************"
client = InferenceClient("meta-llama/Meta-Llama-3-8B-Instruct", token=API_TOKEN)

def run_prompt(prompt):
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500,
        stream=False
    )
    return response.choices[0].message.content

def generate_v4_setting():
    prompt = f"""
        You are to generate a realistic simulation setting for a group of characters with diverse personalities and relationships who are stuck in the same place for an extended period. 
        This setting should form the basis for a real-life simulation where events unfold logically and realistically over time.

        1. **Setting:**
           - The location will be in some reality TV show.
           - Describe the environment where the characters are confined. Consider factors like the size of the space, available resources, and any unique features that could influence the characters' interactions.
           - There might be some limitations or challenges in the environment that could affect the characters' behavior and decisions.
        
        2. **Characters:**
           - Create a list of 5-10 characters with varied backgrounds, personalities, and professions.
           - For each character, specify:
             - Name
             - Age
             - Personality traits (e.g., introverted, extroverted, optimistic, cynical)
             - Background (e.g., profession, personal history)
             - Relationships with other characters (e.g., friends, rivals, romantic interests)
        
        3. **Initial Scenario:**
           - Describe the initial situation when the simulation begins. Include details such as the characters' immediate reactions to being confined and any initial interactions or tensions.
           
        4. **Rules for Events:**
           - Events should unfold in a realistic and logical manner, considering the personalities and relationships of the characters.
           - The simulation should aim to mimic real-life events and interactions, avoiding overly dramatic or implausible scenarios unless naturally arising from the situation.
        
        Remember, the goal is to create a realistic simulation with ordinary events and logical progressions. The events should reflect the natural dynamics and interactions among the characters, evolving over time based on their personalities and relationships.
    """
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500,
        stream=False
    )
    return response.choices[0].message.content


def generate_v3_setting():
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
             * dont be a cliché, dont create a generic setting, dont create stereotypes
             * the goal is to create a setting that feels immersive and generates tension for the characters. The characters themselves should be diverse in personality and skills, with the potential for cooperation, conflict, and unexpected alliances.
             * your answer will be copied as-is so make sure to format it properly and dont include any instructions in the answer.
            """
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500,
        stream=False
    )
    return response.choices[0].message.content


def generate_v2_setting():
    prompt = f"""
    Hi there! I'm working on a simulation project where a group of characters interact within a specific environment. I'd love your help in crafting an engaging setting and defining unique characters that will lead to interesting stories.
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



def generate_v1_setting():
    prompt = f"""
    describe a situation with multiple characters that are stuck in the same place.
    describe in details the setting, the characters, their personalities, their relationships, and a tension factor.
"""
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1500,
        stream=False
    )
    return response.choices[0].message.content



# print(generate_v4_setting())



great_result = f"""
    **Setting:**
    
    The location is a secluded, luxurious villa in the French Riviera, commonly known as "Villa Serenity." The villa is situated on a large plot of land surrounded by lush greenery, with a private beach and a stunning view of the Mediterranean Sea. The interior of the villa features a large living room, a fully equipped kitchen, several bedrooms, and multiple bathrooms.
    
    The villa has the following unique features:
    
    * A state-of-the-art entertainment system with a large screen and top-notch audio equipment
    * A gym and fitness area
    * A private movie theater
    * A beautifully landscaped garden and swimming pool
    * A private beach access with a beachside bar and grill
    
    However, the villa has some limitations and challenges:
    
    * There is no cell phone signal or internet connection within the villa, limiting external communication.
    * The villa's isolation is reinforced by a high-security perimeter fence and 24/7 camera surveillance.
    * The electricity supply is limited, and the villa relies on generator backup during peak usage hours.
    * The villa's main water source is a well, which can be affected by seasonal changes and occasional droughts.
    
    **Characters:**
    
    1. **Alex Chen (Age: 28)**:
        * Personality traits: Optimistic, outgoing, and competitive
        * Background: Professional athlete and reality TV show contestant
        * Relationships: Close friends with Rachel and harmonious acquaintances with the rest of the group
    2. **Rachel Patel (Age: 25)**:
        * Personality traits: Caring, empathetic, and calm
        * Background: Nurse and humanitarian worker, contestant on a previous reality TV show
        * Relationships: Close friends with Alex and Naomi, and has a soft spot for Jack
    3. **Naomi Lee (Age: 30)**:
        * Personality traits: Confident, charismatic, and assertive
        * Background: Businesswoman and entrepreneur, contestant on several reality TV shows
        * Relationships: Competitive with Ariana and friendly with the rest of the group
    4. **Ariana Rodriguez (Age: 29)**:
        * Personality traits: Confident, passionate, and stubborn
        * Background: Activist and artist, contestant on a reality TV show focused on social justice
        * Relationships: Competes with Naomi and has a romantic interest in Jack
    5. **Jack Harris (Age: 32)**:
        * Personality traits: Charismatic, laid-back, and easy-going
        * Background: Musician and entrepreneur, contestant on several reality TV shows
        * Relationships: Has a crush on Rachel and is friendly with the rest of the group
    6. **Sophia Martinez (Age: 27)**:
        * Personality traits: Quirky, creative, and introverted
        * Background: Graphic designer and artist, contestant on a reality TV show focused on art and design
        * Relationships: Close friends with Sophia Rodriguez and a kind audience to the rest of the group
    7. **Sophia Rodriguez (Age: 29)**:
        * Personality traits: Warm, responsible, and caring
        * Background: Chef and culinary instructor, contestant on a cook-off reality TV show
        * Relationships: Close friends with Sophia Martinez and Naomi
    
    **Initial Scenario:**
    
    Upon arrival at Villa Serenity, the contestants are excited and apprehensive about being confined to the villa for an extended period. They are greeted by the show's host, who explains the rules and challenges they will face during their stay.
    
    As they begin to settle in, tensions emerge between Naomi and Ariana, who have a history of competing against each other on previous reality TV shows. Alex and Rachel bond over their shared experiences as reality TV contestants, while Sophia and Sophia Rodriguez chat about their shared love of art and cooking.
    
    Jack is immediately drawn to Rachel and tries to make a good impression, while Naomi is suspicious of his intentions. Ariana is determined to make a romantic connection with Jack, despite his lack of interest. The group's interactions are initially friendly but wary, with everyone trying to adjust to their new surroundings and the unique circumstances of the show.
    
    **Rules for Events:**
    
    * Events will unfold based on the characters' personalities, relationships, and backgrounds.
    * Conflicts and tensions will naturally arise from the unique circumstances of the show, but will be handled in a realistic and logical manner.
    * The simulation will aim to mimic real-life events and interactions, avoiding overly dramatic or implausible scenarios unless naturally arising from the situation.
    * The show's host and producers will periodically intervene to introduce challenges, twists, and surprises, but will not influence the characters' actions or decisions unless absolutely necessary.
"""


def improve_last_setting(setting):
    prompt = f"""
        You are tasked with evaluating and improving a proposed setting for a real-life simulation. The simulation involves a group of characters with diverse personalities and relationships who are confined to the same location for an extended period. The goal of this simulation is to generate realistic and logical events over time, focusing on ordinary interactions rather than dramatic storytelling.

        **Parameters for a Great Setting:**
        1. **Diverse and Well-Defined Characters:**
           - Characters should have distinct and believable personalities, backgrounds, and professions.
           - Relationships between characters should be clearly defined and varied (e.g., friendships, rivalries, romantic interests).
        
        2. **Plausible and Confining Location:**
           - The location should be realistic and provide logical reasons for why the characters are confined.
           - The setting should allow for a range of ordinary activities and interactions.
        
        3. **Initial Scenario and Tension:**
           - The initial situation should set the stage for natural interactions and tensions to develop.
           - Early events should establish character dynamics and potential conflicts.
        
        4. **Realistic and Logical Event Progression:**
           - Events should unfold in a manner consistent with the characters' personalities and relationships.
           - The simulation should prioritize everyday occurrences and interactions, avoiding overly dramatic or implausible scenarios.
        
        Based on these parameters, evaluate the following proposed setting. Identify strengths and weaknesses, and suggest modifications to enhance its realism and potential for generating interesting, ordinary events.
        
        **Proposed Setting:**
        {setting}
        
        Please provide your evaluation and any suggested modifications to improve the setting according to the parameters outlined above.
        You output should be only the new improved setting description.
    """

    return run_prompt(prompt)


# print(improve_last_setting(generate_v4_setting()))
# print(generate_v3_setting())