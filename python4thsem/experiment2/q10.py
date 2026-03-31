# Q10. Replace word 'hi' with 'hello' and remove spaces from beginning and end
sentence = " hi ram hi shyam hi moan "

sentence = sentence.strip()
updated_sentence = sentence.replace("hi", "hello")

print("Updated sentence:")
print(updated_sentence)