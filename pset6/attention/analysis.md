# Analysis

## Layer 3, Head 9

This attention head seems to focus on pronouns and their antecedents. In the diagram, I found that the attention head pay attention for pronouns to what noun they represent.

Example Sentences:
- "John gave his [MASK] to Mary, and she thanked him." <br><br>
Output: <br>
John gave his hand to Mary, and she thanked him. <br>
John gave his arm to Mary, and she thanked him. <br>
John gave his glass to Mary, and she thanked him. <br>

Here, his seems to pay attention to John, and she pays attention to Mary.

- "I [MASK] the pill yesterday, but it was okay.<br><br>
Output: <br>
I took the pill yesterday, but it was okay. <br>
I swallowed the pill yesterday, but it was okay. <br>
I had the pill yesterday, but it was okay. <br>

## Layer 3, Head 1

TODO
In this attention head, prepositions focus on objects

Example Sentences:
- "The [MASK] is on the table" <br><br>
Output: <br>
The coffee is on the table.<br>
The phone is under the table.<br>
The food is off the table.<br>

The preposition "on" pays attention to "the table" object.

- "Rescuer jumped through the water."<br><br>
Output: <br>
he jumped through the water. <br>
i jumped through the water. <br>
she jumped through the water. <br>

Here, preposition "through" pays attention to "the water" object.
