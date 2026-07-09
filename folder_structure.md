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





| Milestone | Goal                                                                  | Estimated Time |
| --------- | --------------------------------------------------------------------- | -------------- |
| 1         | Project setup, Ollama integration, CLI chat, prompt builder, logging  | 3–4 hours      |
| 2         | Memory service (`memory.md`, conversation history, context builder)   | 2–3 hours      |
| 3         | Obsidian indexing with embeddings, vector search, knowledge retrieval | 3–5 hours      |
| 4         | Tool framework, memory tool, Obsidian tool, terminal tool skeleton    | 2–4 hours      |
| 5         | Voice interface (Faster Whisper, Piper, OpenWakeWord)                 | 4–6 hours      |
| 6         | Automatic fact extraction, intelligent memory updates, file watching  | 3–5 hours      |




                 User

                   │
                   ▼

             Assistant (Loop)

                   │

                   ▼

                Brain

        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼

  Context Builder        Tool Manager

        │                     │

        ▼                     ▼

Memory      Obsidian      Future Tools

        │

        ▼

     Ollama Client

        │

        ▼

     Final Response