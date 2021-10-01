# LT2319

The biggest struggle with the assignment was understanding the structure of xml files, and exactly how everything is interconnected. I was somewhat aware of the differences between the files but knowing  how they interact, but a more confusing aspect was knowing what was being handled automatically in the background. At some points I was over-doing it and trying to precisely structure the dialogue. For example, when writing the domain.xml, I thought I was needing to develop a higher-level representation of dialogue, however actually I was meant to write out the different possible combinations of (required) information, depending on the eventual goal of the user. 

The only 'hard-coding' is in the grammar file and this is only on the level of specific phrases. Using the predicates, individuals and so on, the system can automatically handle the rest. 

I was having a bit of trouble understanding the difference between different tags which seemed arbitrary, but I suppose there is some subtle distinction which I don't understand yet. For example, the difference between <question> and <answer> irrelevant at first, but I suppose this indicates to the program whether or not a response is required, as we are not having to handle these aspects of the conversation when writing a DDD. 

In summary, I think the difficulty was in understanding the role of the DDD in relation to the TDM/RASA. I was under the impression that I had to do manage the conversation more than I really needed to.
