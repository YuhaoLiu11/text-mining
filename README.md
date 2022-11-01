# text-mining

Please read the [instructions](instructions.md).
1. Project Overview
I take one of my favorite book that I read when I was in high school, "The Great Gatsby", as the source of my project. In order to summarize this book by counting the number of times a particular word appears in the text, I use a dictionary where the keys are words that appear and the values are frequencies of words in the text. Beside find the frequencies, I also try to find the top 10 words in each text and the words that appear the most in each text that don't appear in other texts. In a word, the technique includes characterizing by word frequencies and computing summary statistics.

2. Implementation
To start with, I search the url code of "The Great Gatspy" and download the context of the book form Project Gutenberg. Then, I make the histrogram that includes the words from a file. During processing the file, I utilize the function of skip_header to read from fp until it finds the line that ends the header, finally returning historgram as the result. To find the total number of the words and number of different words, I define the functon of total_words and different_words to returns the total of the frequencies and the number of different words in a histogram. After getting the result of from total_words and different_words respectively, I figure out that the specific words are still unknown. In order to find out what the specific words that usually appear are, one of the good ideas is using dictionary to count the words. Defining the most_common function helps me on counting what the most common words are, as well as finding the frequencies of the top 10 words. Lastly, I also print out the words in the book that aren't in the word list and other random words from the book.

3. Result
By returning the total words and different words, I get the following result that only shows the number of total words and different words in the book, "The Great Gatsby":

Total number of words: 51111   
Number of different words: 7793

Since knowing the number of words in a book is meaningless, to find out the specific words in the context, I define the most_common function:

The most common words are:
the      2532
and      1564
a        1441
of       1218
to       1197
i        1000
in       848
he       771
was      762
that     566
his      488
it       471
with     461
you      426
at       409
her      377
had      377
on       361
she      353
for      332

Still, the most_common function only shows some of the verbs, pronouns, and prepostitions, which can't helps us to know the main character and other informaiton. To understand the topic and main character of the book, I only print out the top 10 frequently appeared words, showing that:

The most common words are:
said     233
“i       175
gatsby   173
tom      164
daisy    137
one      136
like     116
came     108
back     105
little   102

What interesting is that now I can infer that the main characters of "The Great Gatspy" include Gatsby, Tom, and Daisy. From the word "said" and "like", I also can infer that this is story that is telling about the love, and there are lots of conversation between the different character in the book. The words in the book that aren't in the word list and some random words from the books verify my inference.

4. Reflection
Finding , downloading the sources, and processing the file went smooth. But when I try to find the most common word, I forgot to process stopword list, which causes to print out a lot of meaningless words. What's more, I didn't understand the logic of the code in defining most_common function at the beginning, so there is an error when I run the code. After reviewing the class material, I have a better understanding of what I am writing. I run the debugging and adjust the code again and again until it runs smoothly. Generally speaking, what I learn form this project is by returning the sorted dictionary into a function, it is easy to count the words and give a brief idea of what the booking is telling. Throughout the analyzing the book, it is important to understand the logic and algorithms of the code. With more specific sorted dictionary in the future, I believe I can providing more detailed analysis of each books.