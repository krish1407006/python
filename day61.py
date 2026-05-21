# Asyncio in python

# Asyncio is a library in Python that provides support for asynchronous programming. 
# It allows you to write concurrent code using the async/await syntax.

import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Simulate an asynchronous operation
    print("World")

# Run the asynchronous function
asyncio.run(say_hello())


