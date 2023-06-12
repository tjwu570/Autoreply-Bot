from paddlenlp import Taskflow as tf
from transformers import AutoTokenizer
from paddlenlp.transformers import *
from translate import translate_to_sc as trans
import reply as re


class PaddlePaddle:
    """
    A class that initiates a PaddlePaddle entity, choosing the worktype as sentiment_analysis as default.
    """

    def __init__(self, worktype="sentiment_analysis"):
        """
        Initiating the model, tokenizer, and the classification model.
        Worktype options: https://github.com/PaddlePaddle/PaddleNLP/blob/develop/docs/model_zoo/taskflow.md
        """
        self.worktype = worktype
        self.tokenizer = AutoTokenizer.from_pretrained('ernie-3.0-medium-zh')
        
        match worktype:
            case "sentiment_analysis":
                self.model = tf(worktype)
                print("\nModel sentiment_analysis initiated.\n")
            case "classification":
                self.model = tf("text_classification", task_path='checkpoint/export', is_static_model=True)
    
    def forward(self, input_text):
        """
        The forwarding function that runs the input through the PaddlePaddle model with the chosen worktype.
        """
        if self.worktype == "sentiment_analysis":
            return self.model(input_text)
        elif self.worktype == "classification":
            # return str(str(self.model(input_text)[0]['predictions'][0]['label'])+" "+str(self.model(input_text)[0]['predictions'][0]['score']))
            if self.model(input_text)[0]['predictions'][0]['score'] > 0.3:
                match (str(str(self.model(input_text)[0]['predictions'][0]['label']))):
                    case "caking":
                        #return ["你是說","結塊","嗎"]
                        return [re.caking]
                    case "hair":
                        #return ["你是說","毛髮","嗎"]
                        return [re.hair]
                    case "rust":
                        #return ["你是說","生鏽","嗎"]
                        return [re.rust]
                    case "piece":
                        #return ["你是說","碎屑","嗎"]
                        return [re.piece]
                    case "bug":
                        #return ["你是說","蟲子","嗎"]
                        return [re.bug]
            else:
                if "奶粉" in input_text:
                    return [re.default]
                else:
                    return [re.no_milk_powder]
        # else:
            raise NotImplementedError
        
    def tokenize(self, input_text):
        """
        Word tokenizing.
        """
        return self.tokenizer(input_text)


if __name__ == "__main__":
    # Create an instance of PaddlePaddle
    paddle_paddle = PaddlePaddle(worktype="classification")

    while(1):
        # Get user input
        user_input = trans(input("Enter a sentence: "))
        print("user input:"+user_input)
        # Tokenize user input
        #tokenized_input = paddle_paddle.tokenize(user_input)
        #print(tokenized_input)

        # Forward the input through the model
        replies = paddle_paddle.forward(user_input)
        
        #Print the label
        print("The reply for the input sentence is:", replies)
