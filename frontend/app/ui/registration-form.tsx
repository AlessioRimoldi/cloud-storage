import {lusitana} from '@/app/ui/fonts';
import {
    AtSymbolIcon,
    UserIcon,
    KeyIcon,
    BuildingLibraryIcon,
    BuildingOffice2Icon,
    
} from '@heroicons/react/24/outline';
import {ArrowRightIcon} from '@heroicons/react/20/solid';
import {Button} from '@/app/ui/button';


export default function RegistrationForm(){

    async function createUser(formData: FormData) {

        const rawUserData = {
            email: formData.get('email'),
            username: formData.get('username'),
            organization: formData.get('organization'),
            password: formData.get('password'),
        }

        const response = await 
    }

    return (
    <form className="space-y-3">
        <div className="flex-1 rounded-lg bg-gray-50 px-6 pb-4 pt-8">
                <h1 className={`${lusitana.className} md-3 text-2xl`}>
                    Please register to continue
                </h1>

                <div className="w-full">
                    <div>
                        <label
                        className = "mb-3 mt-5 block text-xs font-medium text-gray-900"
                        htmlFor = "email"
                        >
                            Email
                        </label>
                        <div className='relative'>
                            <input
                                className="peer block w-full rounded-md border border-gray-200 py-[9px] pl-10 text-sm outline-2 placeholder:text-gray-500"
                                id = "email"
                                type = "email"
                                name = "email"
                                placeholder = "Your email"
                                required
                            />
                            <AtSymbolIcon className='pointer-events-none absolute left-3 top-1/2 h-[18px] w-[18px] -translate-y-1/2 text-gray-500 peer-focus:text-gray-900'/>    
                        </div>
                    </div>

                    <div>
                        <label 
                        className="mb-3 mt-5 block text-xs font-medium text-gray-900"
                        htmlFor="username" 
                        >
                            Username
                        </label>
                        <div className="relative">
                            <input 
                            className="peer block w-full rounded-md border border-gray-200 py-[9px] pl-10 text-sm outline-2 placeholder:text-gray-500"
                            id="username"
                            type="text"
                            name="username"
                            placeholder="Username"
                            required
                            />
                            <UserIcon className="pointer-events-none absolute left-3 top-1/2 h-[18px] w-[18px] -translate-y-1/2 text-gray-500 peer-focus:text-gray-900"/>
                        </div>
                    </div>

                    <div>
                        <label
                            className="mb-3 mt-5 block text-xs font-medium text-gray-900"
                            htmlFor="organization"
                        >
                            Organization
                        </label>
                        <div className='relative'>
                            <input
                                className="peer block w-full rounded-md border border-gray-200 py-[9px] pl-10 text-sm outline-2 placeholder:text-gray-500"
                                id="organization"
                                type="text"
                                name="organization"
                                placeholder="Organization"
                            />
                            <BuildingLibraryIcon className='pointer-events-none absolute left-3 top-1/2 h-[18px] w-[18px] -translate-y-1/2 text-gray-500 peer-focus:text-gray-900'/>
                        </div>
                    </div>                
                    <div className="mt-4">
                        <label
                            className="mb-3 block text-xs font-medium text-gray-900"
                            htmlFor="password"
                        >
                            Password
                        </label>
                        <div className ="relative">
                            <input
                                className='peer block w-full rounded-md border border-gray-200 py-[9px] pl-10 text-sm outline-2 placeholder:text-gray-500'
                                id="password"
                                type="password"
                                name="passoword"
                                placeholder="Password"
                                required
                                minLength={6}
                            />
                                <KeyIcon className="pointer-events-none absolute left-3 top-1/2 h-[18px] w-[18px] -translate-y-1/2 text-gray-500 peer-focus:text-gray-900"/>
                        </div>
                </div>
            </div>
            <Button className="mt-4 w-full bg-blue-500" action={createUser}>
                Register <ArrowRightIcon className="ml-auto h-5 w-5 text-gray-50"/>
            </Button>
            <div className = "flex h-8 items-end space-x-1">
                {/*Form for errors here*/}
            </div>
        </div> 
    </form>

    );
}