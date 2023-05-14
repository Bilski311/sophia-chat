import Image from 'next/image'
import FileUploader from './components/FileUploader'

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 w-5/6">
      <FileUploader/>
    </main>
  )
}
