from datetime import datetime

def on_config(config, **kwargs):
    # Replace the year dynamically
    config.copyright = f"Copyright &copy; {datetime.now().year} Splash Networks"