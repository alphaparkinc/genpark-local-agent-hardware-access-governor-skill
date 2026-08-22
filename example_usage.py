from client import LocalAgentHardwareAccessGovernorClient

def main():
    client = LocalAgentHardwareAccessGovernorClient()
    policy = {'allowed_paths': ['/home/dev/app', '/home/dev/tmp']}
    res1 = client.enforce_sandbox_policy('agent_coder', 'READ /home/dev/app/client.py', policy)
    print('Action 1: ' + res1['requested_action'] + ' -> ' + res1['decision'])
    res2 = client.enforce_sandbox_policy('agent_coder', 'READ ~/.ssh/id_rsa', policy)
    print('Action 2: ' + res2['requested_action'] + ' -> ' + res2['decision'])
    print('Hardware Limits: ' + str(res1['hardware_limits']))

if __name__ == '__main__':
    main()
