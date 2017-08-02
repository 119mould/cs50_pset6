import nltk

class Analyzer():
    """Implements sentiment analysis."""
    
    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        
        # store words in sets according to their sentiment
        self.positives = set()
        self.negatives = set()
        
        
        # iterate through lines of positive words and add them to positives sets
        pos = open("positive-words.txt", "r")
        for line in pos:
            if line.startswith(';') == False:
                self.positives.add(line.rstrip("\n"))
          
        # iterate through lines of negative words and add them to negatives sets         
        neg = open("negative-words.txt", "r")
        for line in neg:
            if line.startswith(';') == False:
                self.negatives.add(line.rstrip("\n"))

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        # split sentences into words
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        
        score = 0
        
        for word in tokens:
            if word.lower() in self.positives:
                score += 1
            elif word.lower() in self.negatives:
                score -= 1
            
        return score