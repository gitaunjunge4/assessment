// def a function
function solution(text) {

    // split the text into sentences at the following (. ! ?) characters
    const sentences = text.split(/[.?!]/);

    // set the initial values of max count and max sentence 
    let maxSentence = "";
    let maxWordCount = 0;

    for (const sentence of sentences) { 
    // splitting the sentence into words at empty spaces counts the number of valid words in the sentence
    const words = sentence.split(' ').filter(word => /[a-zA-Z]/.test(word));
    const wordCount = words.length;

    // checks if the word count > than current word count 
    if (wordCount > maxWordCount) {
      maxWordCount = wordCount;
      maxSentence = sentence.trim();
     }
    }

  return console.log(maxSentence);

}   

const text = "This is a sample text. It contains multiple sentences. One of them has the most words! Another sentence.";
solution(text);