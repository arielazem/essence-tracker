# essence-tracker

```bash
poetry init --name "essence-tracker" --description "Identity-based habit tracker" --author "arielazem" --python "^3.10"
poetry add fastapi uvicorn jinja2 httpx
poetry run uvicorn main:app --reload
```