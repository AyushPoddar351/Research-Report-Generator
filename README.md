# Research Report Generator

An autonomous AI-powered research report generation system using LangGraph workflows, multi-agent collaboration, and web research capabilities.

## Features

- **Autonomous Report Generation**: AI agents conduct research and generate comprehensive reports
- **Multi-Agent Workflow**: Specialized analyst personas for different perspectives
- **Web Research Integration**: Real-time web search using Tavily API
- **Interactive Feedback**: Human-in-the-loop feedback during analyst creation
- **Multiple Output Formats**: Generate reports in DOCX and PDF formats
- **Web Interface**: FastAPI-based web application with user authentication
- **Configurable LLMs**: Support for OpenAI, Google Gemini, and Groq models

## Architecture

```
├── research_and_analyst/
│   ├── api/                 # FastAPI web application
│   │   ├── main.py         # FastAPI app entry point
│   │   ├── routes/         # API route handlers
│   │   ├── services/       # Business logic services
│   │   └── templates/      # HTML templates
│   ├── workflows/           # LangGraph workflow definitions
│   │   ├── report_generator_workflow.py  # Main report workflow
│   │   └── interview_workflow.py         # Interview sub-workflow
│   ├── schemas/            # Pydantic models
│   ├── utils/              # Utility functions
│   ├── config/             # Configuration files
│   ├── prompt_lib/         # Prompt templates
│   ├── logger/             # Custom logging
│   └── exception/          # Custom exceptions
├── generated_report/       # Output directory for reports
├── static/                # Web UI assets
├── logs/                  # Application logs
└── users.db              # SQLite user database
```

## Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd Research-report-generator
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment Setup**
```bash
cp .env.copy .env
```

Add your API keys to `.env`:
```env
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_key
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
```

## Configuration

Edit `research_and_analyst/config/configuration.yaml` to customize:

```yaml
llm:
  google:
    provider: "google"
    model_name: "gemini-2.0-flash"
    temperature: 0
    max_output_tokens: 2048
  
  openai:
    provider: "openai"
    model_name: "gpt-4o"
    temperature: 0
  
  groq:
    provider: "groq"
    model_name: "deepseek-r1-distill-llama-70b"
    temperature: 0
    max_output_tokens: 2048

embedding_model:
  provider: "google"
  model_name: "models/text-embedding-004"

retriever:
  top_k: 4
```

## Usage

### Web Application
```bash
uvicorn research_and_analyst.api.main:app --reload
```
Access at `http://127.0.0.1:8000`

**Workflow:**
1. Register/Login to the system
2. Navigate to dashboard
3. Enter research topic and number of analysts
4. Review generated analyst personas
5. Provide feedback or continue
6. Download generated reports (DOCX/PDF)

### Direct Script Execution
```bash
python research_and_analyst/workflows/report_generator_workflow.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Home page |
| `POST` | `/login` | User authentication |
| `GET` | `/dashboard` | Main dashboard |
| `POST` | `/generate_report` | Start report generation |
| `POST` | `/submit_feedback` | Submit human feedback |
| `GET` | `/report_status/{thread_id}` | Check report status |
| `GET` | `/download/{filename}` | Download generated report |

## Workflow Process

1. **Analyst Creation**: AI generates specialized analyst personas based on the research topic
2. **Human Feedback**: Optional human review and feedback on analyst selection
3. **Research Interviews**: Each analyst conducts autonomous research using web search
4. **Report Compilation**: Individual research sections are compiled into a unified report
5. **Content Generation**: Introduction and conclusion are generated
6. **Output Generation**: Final report saved in DOCX and PDF formats

## Dependencies

Key packages:
- `langgraph==0.6.8` - Workflow orchestration
- `langchain-community==0.3.30` - LangChain integrations
- `fastapi==0.120.0` - Web framework
- `tavily-python==0.7.12` - Web search API
- `python-docx==1.2.0` - DOCX generation
- `reportlab==4.4.4` - PDF generation
- `structlog==25.4.0` - Structured logging

## Output Structure

Reports are saved in `generated_report/` with:
```
generated_report/
└── Topic_Name_YYYYMMDD_HHMMSS/
    ├── Topic_Name_YYYYMMDD_HHMMSS.docx
    └── Topic_Name_YYYYMMDD_HHMMSS.pdf
```

Each report contains:
- **Introduction**: Context and overview
- **Research Analysis**: Multi-perspective insights
- **Conclusion**: Key findings and recommendations
- **Sources**: Referenced materials

## Troubleshooting

**Common Issues:**

1. **Memory/State Issues**: Ensure shared memory is properly configured in `ReportService`
2. **API Key Errors**: Verify all required API keys are set in `.env`
3. **Import Errors**: Check Python path and virtual environment activation
4. **Port Conflicts**: Change port in uvicorn command if 8000 is occupied

**Logs**: Check `logs/` directory for detailed error information

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Add tests if applicable
5. Submit pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
- Check the logs in `logs/` directory
- Review configuration in `research_and_analyst/config/`
- Ensure all API keys are properly configured