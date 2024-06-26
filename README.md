## Design for a Flask Application to Teach Language Agent Building

### HTML Files

- `index.html`: The homepage of the website, providing an overview of the purpose and navigation options.
- `building_agents.html`: A page explaining the different steps and concepts involved in building language agents.
- `hands_on_lab.html`: A page with interactive exercises and demonstrations for hands-on practice in building language agents.
- `resources.html`: A page listing additional resources, such as tutorials, forums, and documentation, for further learning and troubleshooting.

### Routes

- `/`: The homepage route, rendering the `index.html` file.
- `/building-agents`: The route for accessing the `building_agents.html` file, providing information on the process of building language agents.
- `/hands-on-lab`: The route for accessing the `hands_on_lab.html` file, allowing users to engage in interactive exercises.
- `/resources`: The route for accessing the `resources.html` file, displaying a list of additional resources.
- `/submit-code`: A POST route designed to handle code submissions from the hands-on exercises, allowing users to check their work and receive feedback.