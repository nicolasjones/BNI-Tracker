import assert from 'node:assert/strict'
import { test } from 'node:test'

function readAiAgentFlag(env = {}) {
  return env.FEATURE_AI_AGENT === 'true'
}

test('AI agent feature flag defaults to disabled', () => {
  assert.equal(readAiAgentFlag({}), false)
})

test('AI agent feature flag enables only with explicit true value', () => {
  assert.equal(readAiAgentFlag({ FEATURE_AI_AGENT: 'true' }), true)
  assert.equal(readAiAgentFlag({ FEATURE_AI_AGENT: '1' }), false)
})
