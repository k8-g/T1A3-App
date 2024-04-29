# Hangman intro ASCII image
intro_image = """                                                                                                                                 
                           #@@@@@@@@@@@@@@@@@@@              
                           #*                =@        
                           #*                =@        
                           #*              #@+-@@      
                           #*             .@    %#     
                           #*              @-   @      
                           #*                @@:       
                           #*                @@.       
                           #*              @@+@#@      
                           #*            @@  =@  @@    
                           #*                =@        
                           #*               -@@%       
                           #*              #@  *@      
                           #*             @*    .@     
                           #*            @:       @    
                           #*                          
                           #*                                       
                      *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

# The different stages of the Hangman gallows from start to finish
hangman_0 = """
   ______
   |    |
   |    
   |   
   |   
   |
   |__________ """

hangman_1 = """
   ______
   |    |
   |    O
   |   
   |   
   |
   |__________ """

hangman_2 = """
   ______
   |    |
   |    O
   |    |
   |   
   |
   |__________ """

hangman_3 = """
   ______
   |    |
   |    O
   |   /|
   |   
   |
   |__________ """

hangman_4 = """
   ______
   |    |
   |    O
   |   /|\ 
   |   
   |
   |__________ """

hangman_5 = """
   ______
   |    |
   |    O
   |   /|\ 
   |   / 
   |
   |__________ """

hangman_6 = """
   ______
   |    |
   |    O
   |   /|\ 
   |   / \ 
   |
   |__________ """
# List of hangman images to be called on in Game.py
hangman_images = [hangman_0, hangman_1, hangman_2, hangman_3, hangman_4, hangman_5, hangman_6]