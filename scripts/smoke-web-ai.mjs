const aiServiceUrl = process.env.AI_SERVICE_URL ?? 'http://localhost:8000'

async function main() {
  const response = await fetch(`${aiServiceUrl}/health`)

  if (!response.ok) {
    throw new Error(`AI service health check failed with HTTP ${response.status}`)
  }

  const body = await response.json()

  if (body.status !== 'ok') {
    throw new Error(`AI service returned unexpected health payload: ${JSON.stringify(body)}`)
  }

  console.log(`AI service reachable at ${aiServiceUrl}`)
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : error)
  process.exit(1)
})
