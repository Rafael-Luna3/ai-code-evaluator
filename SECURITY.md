# Security

AI Code Evaluator executes candidate Python code in a separate subprocess with a configurable timeout.

This provides process separation and timeout control, but it is not a complete security sandbox.

Do not execute arbitrary untrusted code on a sensitive host.

Production use with untrusted submissions should add stronger isolation such as containers, virtual machines, restricted operating-system permissions, resource limits, and network isolation.