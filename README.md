# ✈️ TripMate AI — A Multi-Agent Travel Planner with LangGraph

An open-source AI travel planner that turns a natural-language trip request into a practical travel plan with flight suggestions, hotel ideas, and a day-by-day itinerary.

TripMate AI uses a **multi-agent workflow built with LangGraph and LangChain**, with **OpenAI** powering the language-model capabilities, **AviationStack** for flight research, **Tavily** for hotel/web research, and **SQLite** for local conversation-state persistence.

---

## 🌍 Why This Project?

Planning a trip usually means jumping between multiple websites, travel platforms, search engines, and spreadsheets.

TripMate AI brings this process into one application by coordinating multiple specialized agents:

* ✈️ Flight Search Agent
* 🏨 Hotel Research Agent
* 🗺️ Itinerary Planning Agent
* 🤖 Final Response Agent

These agents work together through a **LangGraph workflow** to generate a practical and structured travel plan from a user's natural-language request.

---

## ✨ Features

* ✈️ **Flight Research** using AviationStack
* 🏨 **Hotel Suggestions** using Tavily Search
* 🧠 **Multi-Agent Orchestration** using LangGraph
* 🔗 **LangChain Integration**
* 🤖 **OpenAI-powered LLM responses**
* 📝 **AI-generated day-by-day travel itineraries**
* 💰 **Budget-aware travel planning**
* 🌐 **FastAPI backend**
* 🖥️ **Simple web interface using Jinja2, HTML, CSS, and JavaScript**
* 💾 **Conversation state persistence using SQLite**
* 🧵 **Thread-based conversation management using LangGraph**
* ⚡ Modular tool-based architecture
* 🔌 Easy integration with additional travel APIs and tools

---

# 🏗️ Architecture

The application follows a sequential multi-agent architecture:

```text
                         ┌───────────────────┐
                         │       User        │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │     FastAPI       │
                         │      Backend      │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │    LangGraph      │
                         │   Orchestrator    │
                         └─────────┬─────────┘
                                   │
                 ┌─────────────────┼─────────────────┐
                 │                 │                 │
                 ▼                 ▼                 ▼
        ┌────────────────┐ ┌────────────────┐ ┌──────────────────┐
        │ Flight Agent  │ │  Hotel Agent   │ │ Itinerary Agent  │
        │                │ │                │ │                  │
        │ AviationStack  │ │    Tavily      │ │     OpenAI       │
        └───────┬────────┘ └───────┬────────┘ └────────┬─────────┘
                │                  │                   │
                └──────────────────┼───────────────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   Final Agent     │
                         │      OpenAI       │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   Final Travel    │
                         │      Plan         │
                         └───────────────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │ SQLite Checkpoint │
                         │   travel_agent.db │
                         └───────────────────┘
```

---

# 🔄 How the Workflow Works

The LangGraph workflow executes the agents sequentially.

```text
START
  │
  ▼
Flight Agent
  │
  ▼
Hotel Agent
  │
  ▼
Itinerary Agent
  │
  ▼
Final Response Agent
  │
  ▼
END
```

### 1. User Request

The user submits a natural-language request such as:

```text
Plan a 3-day trip to Tokyo with a budget of $1200.
```

The request is sent to the FastAPI backend.

### 2. Flight Agent

The Flight Agent processes the user's request and uses **AviationStack** to retrieve flight-related information.

Example:

```text
Origin: DAC
Destination: Tokyo
Travel Duration: 3 days
```

### 3. Hotel Agent

The Hotel Agent uses **Tavily Search** to research hotel options based on the destination and user's requirements.

It can retrieve information such as:

* Hotel names
* Locations
* Approximate prices
* Ratings
* Amenities
* Nearby attractions

### 4. Itinerary Agent

The Itinerary Agent uses the flight and hotel information along with the original user request.

The OpenAI model generates a practical itinerary containing:

* Day-by-day activities
* Attractions
* Travel recommendations
* Suggested activities
* Budget considerations

### 5. Final Response Agent

The Final Agent combines all information and generates the final user-friendly response.

The final response is organized into:

1. Trip Summary
2. Flight Information
3. Hotel Suggestions
4. Day-by-Day Itinerary
5. Estimated Budget
6. Final Recommendations

---

# 🧠 Multi-Agent Design

Each agent has a specific responsibility.

| Agent           | Responsibility      | Technology    |
| --------------- | ------------------- | ------------- |
| Flight Agent    | Flight research     | AviationStack |
| Hotel Agent     | Hotel/web research  | Tavily        |
| Itinerary Agent | Trip planning       | OpenAI        |
| Final Agent     | Response generation | OpenAI        |

This separation makes the system easier to:

* Maintain
* Debug
* Extend
* Test
* Replace individual tools
* Add new agents

---

# 🛠️ Tech Stack

### Backend

* Python 3.10+
* FastAPI
* Uvicorn

### AI / LLM

* OpenAI
* LangChain
* LangGraph

### External APIs

* AviationStack
* Tavily

### Database

* SQLite
* LangGraph SQLite Checkpointer

### Frontend

* Jinja2
* HTML
* CSS
* JavaScript

---

# 📁 Project Structure

```text
TripMate-AI/
│
├── app.py
│   └── FastAPI application entry point
│
├── backend.py
│   └── LangGraph multi-agent travel workflow
│
├── travel_agent.db
│   └── Local SQLite database
│
├── requirements.txt
│   └── Python dependencies
│
├── .env
│   └── Environment variables
│
├── .gitignore
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── index.html
│
└── tools/
    ├── flight_tool.py
    │   └── AviationStack integration
    │
    └── tavily_tool.py
        └── Tavily search integration
```

---

# 📋 Prerequisites

Before running the project locally, make sure you have:

* Python **3.10 or newer**
* An OpenAI API key
* An AviationStack API key
* A Tavily API key

SQLite is included with Python, so **no separate database installation is required**.

You do not need:

* PostgreSQL
* Docker
* Redis
* Any external database server

---

# 🔑 API Keys

TripMate AI requires the following API credentials:

### OpenAI

Used by:

* Itinerary Agent
* Final Response Agent

### AviationStack

Used by:

* Flight Agent

### Tavily

Used by:

* Hotel Research Agent

---

# 🔐 Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key

AVIATIONSTACK_API_KEY=your_aviationstack_api_key

TAVILY_API_KEY=your_tavily_api_key

DEFAULT_ORIGIN_IATA=DAC
```

### Environment Variable Description

| Variable                | Description                          |
| ----------------------- | ------------------------------------ |
| `OPENAI_API_KEY`        | OpenAI API authentication key        |
| `AVIATIONSTACK_API_KEY` | AviationStack API authentication key |
| `TAVILY_API_KEY`        | Tavily API authentication key        |
| `DEFAULT_ORIGIN_IATA`   | Default departure airport IATA code  |

---

# 💾 SQLite Database

TripMate AI uses **SQLite** for LangGraph checkpoint persistence.

The database file is:

```text
travel_agent.db
```

It is created automatically when the application starts.

The SQLite checkpointer is configured using:

```python
import sqlite3

from langgraph.checkpoint.sqlite import SqliteSaver


_conn = sqlite3.connect(
    "travel_agent.db",
    check_same_thread=False
)

checkpointer = SqliteSaver(_conn)

travel_graph = graph.compile(
    checkpointer=checkpointer
)
```

SQLite provides local persistence without requiring a separate database server.

---

# 🧵 Conversation Persistence

LangGraph uses a `thread_id` to maintain conversation state.

For example:

```text
thread_id = user_123
```

The application can maintain checkpoints for this conversation inside:

```text
travel_agent.db
```

Multiple conversations can use different thread IDs:

```text
travel_agent.db
│
├── user_123
│   ├── checkpoint
│   └── conversation state
│
├── user_456
│   ├── checkpoint
│   └── conversation state
│
└── user_789
    ├── checkpoint
    └── conversation state
```

This allows the application to maintain separate conversation states.

---

# 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd TripMate-AI
```

Create a virtual environment:

### Linux / macOS

```bash
python -m venv .venv

source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📚 Required Dependencies

Your `requirements.txt` should include the packages required by the project.

For example:

```text
fastapi
uvicorn
jinja2
python-dotenv

langchain
langchain-openai
langgraph
langgraph-checkpoint-sqlite

tavily-python
requests
```

Add any additional dependencies required by your existing flight tool implementation.

---

# ▶️ Running the Application

Start the FastAPI application:

```bash
python app.py
```

Or using Uvicorn:

```bash
uvicorn app:app --reload
```

The application should be available at:

```text
http://127.0.0.1:8000/
```

Open the URL in your browser.

---

# ❤️ Health Check

The application provides a health-check endpoint:

```text
GET /health
```

Example:

```bash
curl http://127.0.0.1:8000/health
```

---

# ✈️ Travel API

The main travel endpoint is:

```text
POST /api/travel
```

It accepts a natural-language travel request.

### Example Request

```bash
curl -X POST http://127.0.0.1:8000/api/travel \
  -H "Content-Type: application/json" \
  -d '{"message":"Plan a 3-day trip to Tokyo with a budget of $1200"}'
```

### Example User Request

```text
Plan a 5-day trip from Dhaka to Dubai with a budget of $1500.
I want good hotels and popular tourist attractions.
```

The system processes the request through the LangGraph workflow and returns a structured travel plan.

---

# 🧩 LangGraph Workflow

The workflow is implemented using LangGraph's `StateGraph`.

Conceptually:

```python
graph = StateGraph(TrevalState)

graph.add_node(
    "flight_agent",
    flight_agent
)

graph.add_node(
    "hotel_agent",
    hotel_agent
)

graph.add_node(
    "itinerary_agent",
    itinerary_agent
)

graph.add_node(
    "final_agent",
    final_agent
)

graph.add_edge(
    START,
    "flight_agent"
)

graph.add_edge(
    "flight_agent",
    "hotel_agent"
)

graph.add_edge(
    "hotel_agent",
    "itinerary_agent"
)

graph.add_edge(
    "itinerary_agent",
    "final_agent"
)

graph.add_edge(
    "final_agent",
    END
)
```

This creates the following execution flow:

```text
START
  ↓
Flight Agent
  ↓
Hotel Agent
  ↓
Itinerary Agent
  ↓
Final Agent
  ↓
END
```

---

# 🤖 OpenAI Integration

TripMate AI uses OpenAI through LangChain.

Example:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-5-mini"
)
```

The OpenAI model is used for tasks such as:

* Travel planning
* Itinerary generation
* Response formatting
* Combining information from multiple agents

---

# 🔎 Tavily Integration

The Hotel Agent uses Tavily to search for relevant hotel and travel information.

Example:

```text
Best hotels for Tokyo 3 day trip
```

The search results are passed into the LangGraph state and used by the itinerary and final agents.

---

# ✈️ AviationStack Integration

The Flight Agent uses AviationStack for flight-related information.

The flight tool receives the user's travel query:

```python
flight_result = search_flights(
    query=query
)
```

The returned information is stored in the LangGraph state.

---

# 🗃️ State Management

The LangGraph state contains information shared between agents.

Example:

```python
class TrevalState(TypedDict):

    messages: Annotated[
        list[AnyMessage],
        operator.add
    ]

    user_query: str

    flight_results: str

    hotel_results: str

    itinerary: str

    llm_calls: int
```

Each agent reads information from the state and adds its results.

For example:

```text
User Query
    ↓
Flight Results
    ↓
Hotel Results
    ↓
Itinerary
    ↓
Final Response
```

---

# 🔒 Security

Never commit API keys to GitHub.

Add `.env` to `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
travel_agent.db
```

The SQLite database can also be excluded from Git if you don't want to commit local conversation data.

---

# 🚀 Future Improvements

Possible improvements include:

* 🔀 Parallel flight and hotel agents
* 🤖 Dynamic agent routing
* 🧠 Agentic decision-making
* 💰 Real-time flight pricing
* 🏨 Real-time hotel booking
* 🗺️ Google Maps integration
* 🌦️ Weather-aware itinerary planning
* 🚕 Transportation recommendations
* 💳 Currency conversion
* 📍 Location-based recommendations
* 🧑‍💻 User authentication
* 📊 LangSmith observability
* 🧪 Automated agent evaluation
* 🔄 Human-in-the-loop approval
* 💬 Persistent multi-turn conversations
* 🧩 Additional MCP-based travel tools

---

# 🧪 Example

### User

```text
Plan a 3-day trip to Tokyo with a budget of $1200.
I want affordable hotels and popular tourist attractions.
```

### TripMate AI

```text
Trip Summary

Destination: Tokyo
Duration: 3 Days
Budget: $1200

Flight Information

Flight options based on available AviationStack data.

Hotel Suggestions

Recommended budget-friendly hotel options based on
Tavily search results.

Day-by-Day Itinerary

Day 1:
- Visit Shibuya
- Explore Shibuya Crossing
- Visit Meiji Shrine

Day 2:
- Visit Asakusa
- Explore Senso-ji Temple
- Visit Tokyo Skytree

Day 3:
- Visit Tokyo Station
- Explore Ginza
- Shopping and local food

Estimated Budget

Flights: Based on available flight information
Hotels: Based on selected accommodation
Food: Estimated daily budget
Activities: Estimated attraction costs

Final Recommendations

A practical travel plan based on the requested budget.
```

> Flight availability and pricing depend on the data returned by the configured flight API. Ticket prices may not always be available.

---

# 🤝 Contributing

Contributions are welcome!

If you want to improve TripMate AI:

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/new-travel-agent
```

3. Make your changes.
4. Test the application.
5. Commit your changes.

```bash
git commit -m "Add new travel agent"
```

6. Push your branch.

```bash
git push origin feature/new-travel-agent
```

7. Open a Pull Request.

---

# 📄 License

This project is open-source. Add the appropriate license file based on your preferred open-source license.

For example:

```text
MIT License
```

---

# 🙏 Acknowledgments

TripMate AI is built using modern AI and developer technologies, including:

* OpenAI
* LangChain
* LangGraph
* FastAPI
* Tavily
* AviationStack
* SQLite

The project is intended as a practical example of building a **multi-agent AI application with LangGraph**, external tools, API integrations, and persistent conversation state.

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ and sharing it with others interested in:

* Generative AI
* Agentic AI
* LangGraph
* LangChain
* Multi-Agent Systems
* AI Travel Planning
* FastAPI
* LLM Applications
