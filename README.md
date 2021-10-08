# LT2319

- Lab 3:
This assignment was more straight forward given that I had already done lab 2. There were a few tricky parts with errors but it turned out that in almost every case I simply hadn't followed the hints in the instructions properly. 

The one issue I had towards the end was when I was trying to use Rasa. There were some weird errors being thrown, but by changing the grammar a bit, I could avoid these issues, as well as if I avoided using the 'pipeline' endpoint and used the 'tdm' endpoint. I think this was due perhaps to some conficts in the items within different questions, so perhaps the system couldn't determine which one to use? Or perhaps I had updated the grammar but not the rasa model (by not re-running the build command). 

In any case I believe it works as anticipated/intended, but I could work more on adding more training examples which would improve the system. It doesn't seem to handle misspellings very well, but by adding some more work and understanding how rasa builds work, and proviving more examples of incorrect spelling using pre-made data and writing some of my own, I'm sure this system could be built to be very robust and useful. Additionally by adding more features, it would be less likely that a user would come across something which the system is not able to handle. 

Overall I think this system works well, and covers all the base expectations written in the assignment guidelines. 


- Lab 2:
The biggest struggle with the assignment was understanding the structure of xml files, and exactly how everything is interconnected. I was somewhat aware of the differences between the files but knowing, but I realise I was becoming confused by not knowing what was being handled automatically in the background (in terms of the dialogue). At some points I was over-doing it and trying to precisely structure the dialogue. For example, when writing the domain.xml, I thought I was needing to develop a higher-level representation of dialogue (turns to be taken), however instead of writing a structured dialogue, I was just meant to write out the different possible combinations of (required) information, based on the eventual goal of the user. 

The only 'hard-coding' is in the grammar file and this is only on the level of specific phrases. Using the predicates, individuals and so on, the system can automatically handle the rest. 

Additionally, I was having a bit of trouble understanding the difference between different tags (distinctions which seemed arbitrary), but I believe I misunderstood what the DDD and TDM were doing, respectively. For example <question> and <answer> seemed to be the same thing (programatically), when I thought we had to pre-plan/structure the dialogue, but I later learned that it is the system which manages the conversational planning, which is why it is helpful for the program to know whether or not a response is required. 

In summary, I think the difficulty was in understanding the role of the DDD in relation to the TDM/RASA. I was under the impression that I had to do manage the conversation more than I really needed to, and we only need to tell the system what information/services are required (domain), add the slots for retreiving/giving information (grammar), what entities exist (ontology) and initiating external sevices (service interface etc.)
