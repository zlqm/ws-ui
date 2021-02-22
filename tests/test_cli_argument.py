import asyncio
import sys
from unittest.mock import patch

from prompt_toolkit.application import create_app_session
from prompt_toolkit.input import create_pipe_input
from prompt_toolkit.output import DummyOutput
from ws_ui import Application


def test_cli_argument():
    arguments = ['ws-ui']
    with patch.object(sys, 'argv', arguments):
        with create_app_session(input=create_pipe_input(),
                                output=DummyOutput()):
            app = Application()
            asyncio.run(app.main())
            # TODO complete this test case
