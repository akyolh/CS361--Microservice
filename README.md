# Random Exercise Generator Microservice

To request data: Run the request.py file and create an exercises.txt file or download it from here. The code inside request.py can also be directly implemented into the Python file of your original project. Here is an example call:

      time.sleep(1)
      with open('exercises.txt', 'w') as file:
          file.write("get exercise")
      time.sleep(1)
      with open('exercises.txt', 'r') as file:
          exercise = file.read()


To receive data: Run the generate.py file. This is fairly simple and no modification is needed. It will automatically read the exercises.txt file; if "get exercises" is written, it will overwrite it with a random exercise. Once that is complete, the code in request.py will reread the exercises.txt file for the newly generated random exercise. This can be utilized in any way for your code.
