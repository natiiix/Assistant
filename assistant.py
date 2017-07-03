import recognizer
import synthesizer
import expression

def plhldr():
    synthesizer.speak("Expression recognized")

expressions = [expression.expression(plhldr, "hello", "hi", "good morning")]

def process(text):
    for exp in expressions:
        if exp.compare(text):
            exp.action()

while True:
    text = recognizer.listen()
    if text:
        print(text)
        process(text)
