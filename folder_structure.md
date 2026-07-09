jarvis/
│
├── app.py
├── config.py
├── requirements.txt
│
├── core/
│   assistant.py
│   brain.py
│   planner.py
│   context_builder.py
│
├── memory/
│   memory_service.py
│   conversation_store.py
│   long_term_memory.py
│
├── knowledge/
│   obsidian_index.py
│   embeddings.py
│   retriever.py
│
├── llm/
│   ollama_client.py
│   prompts.py
│
├── voice/
│   listener.py
│   speaker.py
│   wakeword.py
│
├── tools/
│   base_tool.py
│   registry.py
│   memory_tool.py
│   obsidian_tool.py
│   terminal_tool.py
│
├── storage/
│   memory.md
│   conversations.json
│   embeddings.sqlite
│
├── vault/
│
├── logs/
│
└── tests/