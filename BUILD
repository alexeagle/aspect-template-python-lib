load("@bazel_lib//lib:run_binary.bzl", "run_binary")
load("@jq.bzl", "jq")
load("@rules_uv//uv:pip.bzl", "pip_compile")

# keep
filegroup(
    name = "requirements",
    srcs = ["requirements.txt"],
    visibility = ["//requirements:__pkg__"],
)

pip_compile(
    name = "pip_compile",
    requirements_in = "pyproject.toml",
    requirements_txt = "requirements.txt",
    visibility = ["//requirements:__pkg__"],
)

# Generate data.json containing build timestamp information.
# Useful with Bazel's --stamp flag.
jq(
    name = "data",
    srcs = [],
    filter = "|".join([
        # Don't directly reference $STAMP as it's only set when stamping
        # This 'as' syntax results in $stamp being null in unstamped builds.
        "$ARGS.named.STAMP as $stamp",
        # Provide a default using the "alternative operator" in case $stamp is null.
        """.TIMESTAMP = ($stamp[0].BUILD_TIMESTAMP // "<unstamped>")""",
    ]),
)

run_binary(
    name = "make_header",
    srcs = [
        "data.json",
        "header.tmpl.txt",
    ],
    outs = ["header.txt"],
    args = [
        "--format=json",
        "-o $(execpath header.txt)",
        "$(execpath header.tmpl.txt)",
        "$(execpath data.json)",
    ],
    tool = "TODO",
    visibility = ["//mylib:__pkg__"],
)
