import { z } from 'zod'

const featureFlagSchema = z.object({
  FEATURE_AI_AGENT: z.string().default('false')
})

export function getFeatureFlags(env: NodeJS.ProcessEnv = process.env) {
  const parsed = featureFlagSchema.parse(env)

  return {
    aiAgentEnabled: parsed.FEATURE_AI_AGENT === 'true'
  }
}
