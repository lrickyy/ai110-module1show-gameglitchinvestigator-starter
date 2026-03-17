# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
   I   - The hint label didn't show up at all, so the label or the show label ticker is broken.
   II  - The hard mode has a lower number than the easy mode so those numbers need to be switched.
   III - Label showed up but only tells the user to go lower
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

ChatGPT chat bot helped with this project. 
An AI suggestion that was correct was showing to me that the program would typecast variables to strings and compare them to int types which would give incorrect results.
An AI suggestion that was incorrect was continuing to use a try-except statement even though it was no longer applicable in the logic of the program. The AI chatbot even recognized this but still left the redundent code because I had asked to fix the try-except statement; not a very good suggestion.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed when I was able to see the program run without the bug. A pytest that was made from ChatGPT was a test to check comparisons between numbers and to check if the number being checked is an int and not a diffferent type. AI was very helpful to helping me understand the logic and how certain cases can cause unforseen results, like numbers larger than the range or negative numbers. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

It is a library that allows you to run custom websites locally on a device.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I want to be very specific with my AI chatbot and make sure that if it finds better solutions to bring them up.
I want to be able to understand the code I am working on before AI makes any big changes that could break the code without me knowing.
AI code can be really helpful in small, localized blocks of code and can give well written sugestions. I would really like to utilize AI for more large-scale projects.
