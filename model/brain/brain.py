import queue
import time
import threading

from ..ai_agents import SpeechToTextAgent, LlamaAgent


class Brain:

    def __init__(self, speech_to_text_agent: SpeechToTextAgent):
        
        self._speech_to_text_agent = speech_to_text_agent
        self._output_text_queue = queue.Queue()

        self._brain_thread = threading.Thread(target=self.run)
        self._brain_thread.start()

        print("init brain...")

    def run(self):
        while True:
            user_input = self._speech_to_text_agent.get_user_text_input()
            if user_input:
                print("user_input", user_input)
                self._llama_agent = LlamaAgent()
                reply = self._llama_agent.get_reply(user_input)
                # reply = user_input
                self._output_text_queue.put(reply)
                print('brain_reply:', reply)

            time.sleep(0.01)

    def get_reply(self):
        if not self._output_text_queue.empty():
            return self._output_text_queue.get()
        return None