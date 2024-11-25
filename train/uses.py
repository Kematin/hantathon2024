from time import time

from safetensors.torch import load_file
from transformers import (
    AutoConfig,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    pipeline,
)


def init_model():
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    # Path to your model file
    model_path = "./results/checkpoint-36/model.safetensors"

    # Load the safetensors model weights manually
    model_weights = load_file(model_path)

    # Load the configuration for BERT
    config = AutoConfig.from_pretrained("bert-base-uncased")

    # Modify the config to match the number of classes in your task
    config.num_labels = (
        9  # This should match the number of classes in your model's fine-tuning task
    )

    # Create a model from the configuration
    model = AutoModelForSequenceClassification.from_config(config)

    # Load the model weights
    model.load_state_dict(model_weights)

    # Now, create a pipeline using the model and tokenizer
    classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

    return classifier


start = time()
classifier = init_model()
end = time()
print(f"[LOG]: LOAD PIPELINE WITH MODEL {end-start} s.")

# Example usage
start = time()
result = classifier("легенду")
print(result)  # Expected output: [{'label': 'turn_on_light', 'score': 0.98}]
end = time()
print(f"[LOG]: GET RESULT {end-start} s.")


"""
label: site_info - index: 0
label: legend_info - index: 1
label: open_card - index: 2
label: disability_group - index: 3
label: path - index: 4
label: legend_place - index: 5
label: search_radius - index: 6
label: detailed_info - index: 7
label: search_place - index: 8

def index_label(index):
    ind = {0: 'site_info', 1: 'legend_info', 2: 'open_card', 3: 'disability_group', 4: 'path', 5: 'legend_place', 6: 'search_radius', 7: 'detailed_info', 8: 'search_place'}
    return ind[index]

"""
