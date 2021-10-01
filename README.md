# LT2319

The biggest struggle with the assignment was understanding the structure of xml files, and exactly how everything is interconnected. I was somewhat aware of the differences between the files but knowing, but I realise I was becoming confused by not knowing what was being handled automatically in the background (in terms of the dialogue). At some points I was over-doing it and trying to precisely structure the dialogue. For example, when writing the domain.xml, I thought I was needing to develop a higher-level representation of dialogue (turns to be taken), however instead of writing a structured dialogue, I was just meant to write out the different possible combinations of (required) information, based on the eventual goal of the user. 

The only 'hard-coding' is in the grammar file and this is only on the level of specific phrases. Using the predicates, individuals and so on, the system can automatically handle the rest. 

Additionally, I was having a bit of trouble understanding the difference between different tags (distinctions which seemed arbitrary), but I believe I misunderstood what the DDD and TDM were doing, respectively. For example <question> and <answer> seemed to be the same thing (programatically), when I thought we had to pre-plan/structure the dialogue, but I later learned that it is the system which manages the conversational planning, which is why it is helpful for the program to know whether or not a response is required. 

In summary, I think the difficulty was in understanding the role of the DDD in relation to the TDM/RASA. I was under the impression that I had to do manage the conversation more than I really needed to, and we only need to add the slots for retreiving/giving information and initiating external sevices. 
