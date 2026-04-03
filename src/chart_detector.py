import openai

class ChartDetector:
    def __init__(self, api_key):
        openai.api_key = api_key

    def detect_and_analyze(self, image_path):
        # Load the image and use OpenAI's vision API for analysis
        analysis = openai.Image.create(
            file=open(image_path, 'rb'),
            purpose='detect_chart'
        )
        return analysis['data']

    def generate_questions(self, analysis):
        questions = []
        # Example of generating questions based on chart analysis
        for item in analysis:
            questions.append(f"What is the main trend shown in the chart titled '{item['title']}'?")
            questions.append(f"What data points are represented in the chart?")
        return questions

if __name__ == '__main__':
    detector = ChartDetector(api_key='YOUR_API_KEY')
    result = detector.detect_and_analyze('chart_image.png')
    questions = detector.generate_questions(result)
    for question in questions:
        print(question)
