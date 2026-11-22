import ollama
y = 1
while(y):
    x = input()
    if x == "bye":
        break
    response = ollama.chat(
        model = "llama3.2",
        messages = [{"role" : "user",
                    "content" : f"{x}"}],
        )
    print(response["message"]["content"])
    print("if you want to end the conversion enter {bye}")

