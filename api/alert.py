from jinja2 import Environment, FileSystemLoader

class Alert:
    def __init__(self, alert_raw_data, alert_classification, network_data):
        self.alert_raw_data = alert_raw_data
        self.alert_classification = alert_classification
        self.network_data = network_data

    @property
    def agent_name(self):
        return self.alert_raw_data.get("agent").get("name")

    def to_dict(self):
        return {
            "alert_raw_data": self.alert_raw_data,
            "alert_type": self.alert_classification.get("type"),
            "alert_trigger": self.alert_classification.get("trigger"),
            "networkgraph": self.network_data["networkgraph"],
            "networkroutes": self.network_data["networkroutes"]
        }
    
    def generate_prompt(self):
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('one-shot.prompt')
        data = self.to_dict()
        prompt = template.render(data)
        return prompt