from langchain.prompts import PromptTemplate
from langchain_community.llms import LlamaCpp


class LlamaAgent:

    def __init__(self, model_path="models/llama-2-7b.Q4_K_M.gguf", prompt_path = "prompts/example-en.txt"):

        self._model_path = model_path
        self._prompt_path = prompt_path

        self._llm = LlamaCpp(
            model_path=self._model_path,
            n_gpu_layers=16, # Metal set to 1 is enough.
            n_batch=512,    # Should be between 1 and n_ctx, consider the amount of RAM of your Apple Silicon Chip.
            n_ctx=4096,     # Update the context window size to 4096
            f16_kv=True,    # MUST set to True, otherwise you will run into problem after a couple of calls
            # callbacks=callback_manager,
            stop=["<|im_end|>"],
            verbose=False,
        )

        with open(prompt_path, 'r', encoding='utf-8') as file:
            template = file.read().strip() # {dialogue}
        self._prompt_template = PromptTemplate(template=template, input_variables=["dialogue"])

        self._dialogue = ""

    def get_reply(self, user_input):
        self._dialogue += "*Q* {}\n".format(user_input)
        prompt = self._prompt_template.format(dialogue=self._dialogue)
        reply = self._llm.invoke(prompt, max_tokens=4096)
        if reply is not None:
            self._dialogue += "*A* {}\n".format(reply)
        return reply

