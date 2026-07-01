const requiredVariables = [
  'NEXT_PUBLIC_APP_URL',
  'AI_SERVICE_URL',
  'AI_SERVICE_ENV',
  'AI_PROVIDER'
]

const missingVariables = requiredVariables.filter((key) => !process.env[key])

if (missingVariables.length > 0) {
  console.error(`Missing required environment variables: ${missingVariables.join(', ')}`)
  process.exit(1)
}

console.log('Required environment variables are present.')
