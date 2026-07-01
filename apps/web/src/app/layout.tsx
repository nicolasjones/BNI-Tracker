import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'BNI Track',
  description: 'Base técnica para BNI Track'
}

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  )
}
