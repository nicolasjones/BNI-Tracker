import { getFeatureFlags } from '@/lib/config'

export default function HomePage() {
  const flags = getFeatureFlags()

  return (
    <main style={{ maxWidth: 960, margin: '0 auto', padding: '64px 24px' }}>
      <p style={{ color: '#be0f34', fontWeight: 700, letterSpacing: 1, textTransform: 'uppercase' }}>
        BNI Track
      </p>
      <h1 style={{ fontSize: 48, lineHeight: 1.05, margin: '12px 0' }}>
        Base técnica lista para construir el MVP.
      </h1>
      <p style={{ color: '#667085', fontSize: 18, lineHeight: 1.6 }}>
        Esta aplicación Next.js queda separada del servicio de IA FastAPI y de Supabase para preservar límites claros entre UI, orquestación de IA y datos.
      </p>
      <section style={{ display: 'grid', gap: 16, marginTop: 32, gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))' }}>
        {[
          ['Web app', 'Next.js + TypeScript para la experiencia de producto.'],
          ['AI service', 'FastAPI con gateway agnóstico de proveedor.'],
          ['Guardrails', 'Scripts de calidad, tests, Docker y CI base.']
        ].map(([title, description]) => (
          <article key={title} style={{ background: 'white', borderRadius: 16, padding: 24, boxShadow: '0 12px 32px rgba(16,24,40,0.08)' }}>
            <h2 style={{ marginTop: 0 }}>{title}</h2>
            <p style={{ color: '#667085' }}>{description}</p>
          </article>
        ))}
      </section>
      <p style={{ marginTop: 32, color: '#667085' }}>
        Agente IA: <strong>{flags.aiAgentEnabled ? 'habilitado' : 'deshabilitado'}</strong>
      </p>
    </main>
  )
}
