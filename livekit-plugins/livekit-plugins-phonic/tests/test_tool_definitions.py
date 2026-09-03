from livekit.agents import llm
from livekit.plugins.phonic.realtime import to_phonic_tool_definitions


def test_to_phonic_tool_definitions() -> None:
    @llm.function_tool(name="topicComplete", description="Mark the topic complete.")
    async def topic_complete(reason: str) -> str:
        return reason

    definitions = to_phonic_tool_definitions(llm.ToolContext([topic_complete]))

    assert definitions == [
        {
            "name": "topicComplete",
            "description": "Mark the topic complete.",
            "parameters": {
                "type": "object",
                "properties": {"reason": {"type": "string"}},
                "required": ["reason"],
                "additionalProperties": False,
            },
        }
    ]


def test_to_phonic_tool_definitions_allows_no_description() -> None:
    @llm.function_tool(name="topicComplete")
    async def topic_complete() -> None:
        pass

    assert to_phonic_tool_definitions(llm.ToolContext([topic_complete]))[0]["description"] == ""
