import asyncio
import os
from typing import Literal

from livekit import rtc
from livekit.agents import llm
from livekit.agents.types import NOT_GIVEN, NotGivenOr


class STSModel(llm.RealtimeModel):
    def __init__(
        self,
        api_key: str | None = None,
    ) -> None:
        super().__init__(
            capabilities=llm.RealtimeCapabilities(
                message_truncation=False,
                turn_detection=True,
                user_transcription=True,
                auto_tool_reply_generation=True,
                audio_output=True,
                manual_function_calls=False,
            )
        )

        self.api_key = api_key or os.getenv("PHONIC_API_KEY")

    @property
    def model(self) -> str:
        return "phonic-echo-sts-model"

    @property
    def provider(self) -> str:
        return "phonic"

    def session(self) -> llm.RealtimeSession:
        pass

    async def aclose(self) -> None:
        pass


class STSSession(llm.RealtimeSession):
    def __init__(self, realtime_model: llm.RealtimeModel) -> None:
        super().__init__()

    @property
    def chat_ctx(self) -> llm.ChatContext:
        pass

    @property
    def tools(self) -> llm.ToolContext:
        pass

    async def update_instructions(self, instructions: str) -> None:
        pass

    async def update_chat_ctx(
        self, chat_ctx: llm.ChatContext
    ) -> None:
        pass

    async def update_tools(self, tools: list[llm.Tool]) -> None:
        pass

    def update_options(self, *, tool_choice: NotGivenOr[llm.tool_context.ToolChoice | None] = NOT_GIVEN) -> None:
        pass

    def push_audio(self, frame: rtc.AudioFrame) -> None:
        pass

    def push_video(self, frame: rtc.VideoFrame) -> None:
        pass

    def generate_reply(
        self,
        *,
        instructions: NotGivenOr[str] = NOT_GIVEN,
    ) -> asyncio.Future[llm.realtime.GenerationCreatedEvent]:
        pass

    def commit_audio(self) -> None:
        pass

    def commit_user_turn(self) -> None:
        pass

    def clear_audio(self) -> None:
        pass

    def interrupt(self) -> None:
        pass

    def truncate(
        self,
        *,
        message_id: str,
        modalities: list[Literal["text", "audio"]],
        audio_end_ms: int,
        audio_transcript: NotGivenOr[str] = NOT_GIVEN,
    ) -> None:
        pass

    async def aclose(self) -> None:
        pass

    def start_user_activity(self) -> None:
        """notifies the model that user activity has started"""
        pass
