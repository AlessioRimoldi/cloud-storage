import Logo from '@/app/ui/logo';
import LoginForm from './ui/login-form';
import RegistrationForm from './ui/registration-form';
import {lusitana} from '@/app/ui/fonts';

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col p-6">
      <div className="flex h-20 shrink-0 items-end rounded-lg bg-gray-500 p-4 md:h-52">
        <Logo />
      </div>
      <div className="mt-4 flex grow flex-col gap4 md:flex-row">
        <div className="flwx flex-col justify-center gap-6 rounded-lg bg-gray-50 p-6 md:px-20">
          <p className={`${lusitana.className} text-xl text-gray-800 md:text-3xl md:leading-normal`}>
            <strong> Welcome to the Cloud Research Platform</strong> You can find the code at{' '}
            <a href="https://github.com/AlessioRimoldi/cloud-storage" className='text-blue-500'>
              Github Repository
            </a>
            , by Alessio Rimoldi
          </p>
        </div>
      </div>

      <div className='flex items-center justify-center p-6 md:w-3/5 md:px-28 md:py-12'>
        <div className='flex flex-col gap-6 w-full'>
          <div className='flex flex-col gap-6'>
            <LoginForm className="bg-blue-500"/>
          </div>
          <div className='flex flex-col gap-6'>
            <RegistrationForm />
          </div>
        </div>
      </div>


    </main>
  );
}
