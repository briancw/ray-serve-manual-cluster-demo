from starlette.requests import Request
import ray
from ray import serve
from llama_cpp import Llama
import json

@serve.deployment(num_replicas=1, ray_actor_options={"num_gpus": 1})
class Wat:
    def __init__(self):
        # Load Model
        self.model = Llama(model_path="/models/llama-2-7b.Q4_K_M.gguf", n_gpu_layers=128)

    def dostuff(self, text: str) -> str:
        # Do Stuff
        output = self.model.create_completion(prompt=text, stream=False, max_tokens=32)
        return output

    async def __call__(self, http_request: Request) -> str:
        wat_json: str = await http_request.json()
        prompt = wat_json["prompt"]
        return self.dostuff(prompt)

wat_app = Wat.bind()
