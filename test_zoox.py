from click.testing import CliRunner
from zoox import cli

TEST_LINE_ORIGINAL_1 = ''
TEST_LINE_ORIGINAL_2 = ''

def test_zoox():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('original.txt', 'w') as o:
            o.write(TEST_LINE_ORIGINAL_1)
            o.write(TEST_LINE_ORIGINAL_2)

        result = runner.invoke(cli, ['-t tsv', 'original.txt'])
        assert result.exit_code == 0
        assert 'Zoox created a new tsv file:' in result.output
