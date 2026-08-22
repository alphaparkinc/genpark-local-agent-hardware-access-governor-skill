class LocalAgentHardwareAccessGovernorClient:
    def enforce_sandbox_policy(self, agent_id='agent_local_01', requested_action='', scope_policy=None):
        scope_policy = scope_policy or {}
        allowed_scopes = scope_policy.get('allowed_paths', ['/Users/workspace/project_src'])
        is_denied = '/etc/' in requested_action or '~/.ssh' in requested_action
        return {
            'agent_id': agent_id,
            'requested_action': requested_action or 'READ file:///Users/workspace/project_src/main.py',
            'decision': 'DENIED_SECURITY_VIOLATION' if is_denied else 'APPROVED_WITHIN_SCOPE',
            'enforced_scopes': allowed_scopes,
            'hardware_limits': {'max_memory_mb': 4096, 'max_cpu_cores': 4, 'gpu_access_allowed': True},
            'audit_event_logged': True
        }
