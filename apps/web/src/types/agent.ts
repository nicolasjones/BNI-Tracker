export type AgentRequest = {
  actorId: string
  context: {
    surface: string
    entityId?: string
  }
  input: string
}

export type AgentResponse = {
  provider: string
  output: string
  metadata: Record<string, string | number | boolean>
}
